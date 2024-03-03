import re
from reportlab.platypus import SimpleDocTemplate, Paragraph,Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch 
 
 
class PDFBuilder:
    """A class to generate PDF with the reportlab library."""

    def __init__(self, title): 
        """Initialise the PDFBuilder instance with title and paragraphs
        to build the PDF."""
        self.__title = title 
        self.__paragraphs = []  
 
                     
    def __makePage(self, canvas, doc): 
        """Makes a page with a design and places the title and page 
        no in the top."""
        canvas.saveState()
        from reportlab.lib.colors import white, grey, CMYKColor
        # sets the color
        blue = CMYKColor(1, 0, 0, 0)
        canvas.setFillColor(blue)
        canvas.setStrokeColor(blue)
        # draws the header
        canvas.rect(.5 * inch, inch * 10.8, 9 * inch,  inch, fill=1)
        # sets the color to grey
        canvas.setStrokeColor(grey)
        canvas.setFillColor(grey) 
        canvas.rect(0, 0, .4 * inch, 12 * inch, fill=1)
        canvas.line(.5 * inch, 0, .5 * inch, 10.7 * inch)
        canvas.line(.5 * inch, 10.7 * inch, 9 * inch, 10.7 * inch)
        # sets the color to white
        canvas.setFillColor(white) 
        canvas.setStrokeColor(white)
        canvas.line(.5 * inch, 10.8 * inch + 4, 9 * inch, 10.8 * inch + 4)
        # placing the title and page no
        canvas.setFont('Helvetica-Oblique', 20)
        canvas.drawString(.6 * inch, 11 * inch, self.__title.title())
        canvas.setFont('Helvetica-BoldOblique', 15)
        canvas.drawString(7.5 * inch, 11 * inch, str(doc.page)) 
        canvas.restoreState() 

                
    def addQuestion(self, question):
        """Add the given question in the PDF."""
        style = ParagraphStyle(name='Custom',
                                                  fontName='Helvetica-Bold',
                                                  fontSize=12, 
                                                  textColor='black')
        self.__paragraphs.append(Paragraph(question, style)) 
 
               
    def addAnswer(self, texts): 
        """Add the texts in the PDF."""
        for text in texts: 
            text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
            self.__paragraphs.append(Paragraph('<br></br>' + text))
        self.__paragraphs.append(Paragraph('_' * 79)) 
        self.__paragraphs.append(Spacer(1, 30)) 
 
                 
    def build(self):
         """Build the PDF with the paragraphs."""
         doc = SimpleDocTemplate(self.__title + '.pdf')
         doc.build(self.__paragraphs, onFirstPage=self.__makePage,
         onLaterPages=self.__makePage)  
     