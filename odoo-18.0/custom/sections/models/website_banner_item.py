from odoo import models, fields

class WebsiteBannerItem(models.Model):
    _name = 'website.banner.item'
    _description = 'Banner Image/Link Item'
    _order = 'sequence'

    banner_id = fields.Many2one('website.banner', string='Banner', required=True, ondelete='cascade')
    image = fields.Image(string='Image', required=True)
    title = fields.Char(string='Title')
    link_url = fields.Char(string='Link URL')
    sequence = fields.Integer(string='Order in Banner', default=10)
    active = fields.Boolean(string='Active', default=True)
