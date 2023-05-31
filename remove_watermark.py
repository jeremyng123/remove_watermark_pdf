import sys
import fitz

# https://github.com/pymupdf/PyMuPDF/discussions/1855
word = sys.argv[1]  # search string
input_filname = sys.argv[2]
output_filename = sys.argv[3]
doc = fitz.open(input_filname)
assert isinstance(doc, fitz.Document)
for page in doc:
    page.clean_contents()
    xref = page.get_contents()[0]  # get xref of resulting /Contents object
    cont = bytearray(page.read_contents()
                     )  # read the contents source as a (modifiable) bytearray
    # print(xref, cont)
    if cont.find(
            b"/Subtype/Watermark"
    ) > 0:  # this will confirm a marked-content watermark is present
        print(f"marked-content watermark present at {page.number}")
    while True:
        i1 = cont.find(
            b"/Artifact <</Subtype"
        )  # start of definition. Needs to incude <</Subtype because there are other /Artifacts that are not watermarks
        if i1 < 0: break  # none more left: done
        i2 = cont.find(b"EMC", i1)  # end of definition
        whitespace_len = i2 + 3 - (i1 - 2 + 1)
        # remove the full definition source "q ... EMC"
        # in the issue, the author merely removed with a blank string.
        # However, just removing the target string causes unexpected errors freezed operations
        # By replaciong the target string with the same length of whitespace, the program
        # avoids freezing and continued operations
        cont[i1 - 2:i2 + 3] = b" " * whitespace_len
        doc.update_stream(xref, cont)  # replace the original source
doc.save(output_filename, clean=True, garbage=3)  # save to new file
print("docsaved!")