from odoo import models, fields, api

from odoo import models, fields
from odoo.exceptions import ValidationError

class WebsiteSection(models.Model):
    _name = 'website.section'
    _description = 'Website Section'
    _order = 'sequence'

    name = fields.Char(string='Section Title', required=True)
    section_type = fields.Selection([
        ('type1', '1 Banner'),
        ('type2', '2 Banners'),
        ('type3', '3 Banners'),
        ('type4', '4 Banners'),
    ], string='Section Type', required=True)
    banner_ids = fields.One2many('website.banner', 'section_id', string='Banners')
    sequence = fields.Integer(string='Display Order', default=10)
    active = fields.Boolean(string='Active', default=True)

    @api.constrains('banner_ids')
    def _check_banner_limit(self):
        for rec in self:
            if len(rec.banner_ids) > 4:
                raise ValidationError("A section can have a maximum of 4 banners.")

    def action_open_banners(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Banners',
            'view_mode': 'tree,form',
            'res_model': 'website.banner',
            'domain': [('section_id', '=', self.id)],
            'context': {
                'default_section_id': self.id
            },
            'target': 'current'
        }