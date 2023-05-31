import PyPDF2
from PyPDF2.generic import ContentStream, NameObject, TextStringObject, IndirectObject
import sys

#######
# Author: jeremyng123
# Contact https://github.com/jeremyng123
#
#######


def Remove_Watermark(filename, wm_subtext, wm_bsubtext):
    with open(filename, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

    # https://stackoverflow.com/questions/37752604/watermark-removal-on-pdf-with-pypdf2
    for page in reader.pages:
        # Get the current page's contents
        content_object = page["/Contents"]
        content = ContentStream(content_object, reader)

        # # Loop over all pdf elements
        for operands, operator in content.operations:
            if operator == b"TJ":
                text = operands[0][0]
            else:
                text = operands
            if operator == b"BDC":
                try:
                    ## In the unlikely event that BDC contains the string, uncomment the below block
                    # if isinstance(text, PyPDF2.generic._base.TextStringObject) and wm_subtext in text.lower():
                    #     operands[0] = TextStringObject("")
                    # elif isinstance(text, PyPDF2.generic._base.ByteStringObject) and wm_bsubtext in text.lower():
                    #     operands[0] = TextStringObject("")
                    # elif operands[0] == '/Artifact' and len(operands) >1 and isinstance(operands[1], dict) and '/Subtype' in operands[1].keys() and operands[1]['/Subtype'] == "/Watermark":
                    #     operands[1] = NameObject(' ')
                    ###############################################################################################################

                    # Comment out below if you are uncommenting the block above
                    if operands[0] == '/Artifact' and len(
                            operands) > 1 and isinstance(
                                operands[1],
                                dict) and '/Subtype' in operands[1].keys(
                                ) and operands[1]['/Subtype'] == "/Watermark":
                        operands[1] = NameObject(' ')
                except Exception as e:
                    print(e)
                    pass
            try:
                if isinstance(text, PyPDF2.generic._base.TextStringObject
                              ) and wm_subtext in text.lower():
                    operands[0] = TextStringObject("")
                elif isinstance(text, PyPDF2.generic._base.ByteStringObject
                                ) and wm_bsubtext in text.lower():
                    operands[0] = TextStringObject("")
            except Exception as e:
                pass
            if isinstance(text,
                          TextStringObject) and wm_subtext in text.lower():
                operands[0] = TextStringObject("")
            elif isinstance(text, PyPDF2.generic._base.ByteStringObject
                            ) and wm_bsubtext in text.lower():
                operands[0] = TextStringObject("")

        # # Set the modified content as content object on the page
        page.__setitem__(NameObject("/Contents"), content)

        # Add the page to the output
        writer.add_page(page)

    with open('new-fml.pdf', 'wb') as output_file:
        writer.write(output_file)


def main():
    if len(sys.argv) < 3:
        print('Usage: python remove_watermark.py filename.pdf wm_subtext')
        return
    # Required configurations!
    wm_subtext = sys.argv[2]
    wm_bsubtext = bytes(wm_subtext, "utf-8")
    Remove_Watermark(sys.argv[1], wm_subtext, wm_bsubtext)


if __name__ == "__main__":
    main()
