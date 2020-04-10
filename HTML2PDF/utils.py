from io import BytesIO # A stream implementation using an in-memory bytes buffer
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa # pisa is a html2pdf converter uses the ReportLab Toolkit, HTML5lib and pyPDF

def render_to_pdf(template_src, context_dict = {'pagesize':'A4'}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if(not pdf.err):
        return HttpResponse(result.getvalue(), content_type = 'application/pdf')
    return None


