
#import win32com.client
#doc = win32com.client.GetObject("WWFC\Code of Conduct\Resepct - Spectators.docx")
#doc.SaveAs (FileName="Resepct - Spectators.html", FileFormat=8)
#doc.Close ()

import mammoth
import os

directory = "WWFC"

#custom_styles = "b => i"

for subdir, dirs, files in os.walk(directory):
    for file in files:
        filepath = subdir + os.sep + file

        print (filepath)
        if filepath.endswith(".docx"):
            print ("here")
            output_filename = filepath.removesuffix(".docx") + ".html"

            with open(filepath, "rb") as docx_file:
                result = mammoth.convert_to_html(docx_file)

                text = result.value
                with open(output_filename, 'w') as html_file:
                    html_file.write(text)

