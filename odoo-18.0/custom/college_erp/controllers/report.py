# controllers/report.py
from odoo import http
from odoo.http import request, route




class StudentReportController(http.Controller):

    @route('/college/student/report/<int:student_id>',
           type='http',
           auth='user',
           website=False)
    def student_report(self, student_id, **kwargs):
        student = request.env['college.student'].browse(student_id)
        if not student.exists():
            return request.not_found()

        return request.render(
            'college_erp.student_report_template',
            {'student': student}
        )