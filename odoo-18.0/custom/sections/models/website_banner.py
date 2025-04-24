from odoo import models, fields

class WebsiteBanner(models.Model):
    _name = 'website.banner'
    _description = 'Website Banner'
    _order = 'sequence'

    section_id = fields.Many2one('website.section', string='Section', required=True, ondelete='cascade')
    name = fields.Char(string='Banner Title', required=True)
    item_ids = fields.One2many('website.banner.item', 'banner_id', string='Banner Items')
    sequence = fields.Integer(string='Order in Section', default=10)
    active = fields.Boolean(string='Active', default=True)
