from odoo import http
from odoo.http import request

class WebsiteHeroController(http.Controller):

    @http.route('/hero/preview', type='http', auth='public', website=True)
    def hero_preview(self, **kwargs):
        sections = request.env['website.section'].sudo().search([('active', '=', True)], order='sequence')
        return request.render('sections.hero_section_template', {
            'sections': sections,
        })