from odoo import http, fields
from odoo.http import request
from datetime import date,datetime
import logging
_logger = logging.getLogger(__name__)

class StudentController(http.Controller):
    @http.route('/api/students/filter', auth='public', type='json', methods=['POST'], csrf=False)
    def filter_students(self):
        data = request.get_json_data()
        _logger.info("Received data: %s", data)

        name_contains = data.get('name_contains')
        created_today = data.get('created_today')
        show_all = data.get('show_all')

        domain = []
        if not show_all:
            if name_contains:
                domain.append(('name', 'ilike', name_contains))
            if created_today:
                today = fields.Date.today()
                domain.append(('create_date', '>=', today))


        students = request.env['college.student'].sudo().search(domain)
        _logger.info("✅ Students fetched: %s", students)

        student_data = [{
            'id': student.id,
            'name': student.name,
            'roll_number': student.roll_number,
            'email': student.email,
            'course': student.course,
            'state': student.state,
            'create_date': student.create_date.strftime('%Y-%m-%d') if student.create_date else ''
        } for student in students]

        return {'students': student_data}
