
from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date
import logging
_logger = logging.getLogger(__name__)



class CollegeStudent(models.Model):
    _name = 'college.student'
    _description = 'College Student'

    name = fields.Char(string="Name", required=True)
    image_1920 = fields.Image(string="Profile Photo")
    roll_number = fields.Char(string="Roll Number", required=True)
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute="_compute_age", store=True)
    course = fields.Char(string="Course")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('alumni', 'Alumni')],
        string='Status', default='draft', tracking=True)

    def action_view_report(self):
        self.ensure_one()
        if not self.id:
            raise UserError(_("Please save the student record first"))
        return {
            'type': 'ir.actions.act_url',
            'url': f'/college/student/report/{self.id}',
            'target': 'new',
        }

    @api.depends('date_of_birth')
    def _compute_age(self):
        for student in self:
            if student.date_of_birth:
                today = date.today()
                born = student.date_of_birth
                student.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

                # Automatically update state if age >= 21
                if student.age >= 21 and student.state != 'alumni':
                    student.state = 'alumni'
            else:
                student.age = 0

    @api.model
    def create(self, vals):
        if not vals.get('roll_number'):
            # Get last student ordered by roll number descending
            last_student = self.search([], order="roll_number desc", limit=1)
            if last_student and last_student.roll_number.isdigit():
                new_roll = str(int(last_student.roll_number) + 1).zfill(4)
            else:
                new_roll = '0001'
            vals['roll_number'] = new_roll
        return super().create(vals)

    @api.constrains('email')
    def _check_email_unique(self):
        for student in self:
            if student.email:
                existing = self.env['college.student'].search([
                    ('email', '=', student.email),
                    ('id', '!=', student.id)
                ], limit=1)
                if existing:
                    raise UserError(_("Email must be unique. '%s' is already used by another student.") % student.email)

    def write(self, vals):
        for student in self:
            # Ensure age is up-to-date
            if student.date_of_birth:
                today = date.today()
                born = student.date_of_birth
                age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

                # Check if age >= 21 and student not already alumni
                if age >= 21 and vals.get('state') != 'alumni' and student.state != 'alumni':
                    vals['state'] = 'alumni'

                    # Log info when promoted
                    _logger.info(f"Student {student.name} was marked as Alumni due to age >= 21.")

        return super().write(vals)


