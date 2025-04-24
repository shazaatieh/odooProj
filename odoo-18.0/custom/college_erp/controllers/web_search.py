from odoo import http
from odoo.http import request, route

class StudentSearchPage(http.Controller):

    @route('/college/student/search', type='http', auth='public', website=True)
    def student_search_page(self, **kwargs):
        print("🔍 Student search page loaded")

        return request.render('college_erp.student_search_template', {})