# -*- coding: utf-8 -*-
# from odoo import http


# class TesSkill(http.Controller):
#     @http.route('/tes_skill/tes_skill/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tes_skill/tes_skill/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tes_skill.listing', {
#             'root': '/tes_skill/tes_skill',
#             'objects': http.request.env['tes_skill.tes_skill'].search([]),
#         })

#     @http.route('/tes_skill/tes_skill/objects/<model("tes_skill.tes_skill"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tes_skill.object', {
#             'object': obj
#         })
