# -*- coding: utf-8 -*-
from odoo import http

# class VitAutoBackupUpload(http.Controller):
#     @http.route('/vit_auto_backup_upload/vit_auto_backup_upload/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_auto_backup_upload/vit_auto_backup_upload/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_auto_backup_upload.listing', {
#             'root': '/vit_auto_backup_upload/vit_auto_backup_upload',
#             'objects': http.request.env['vit_auto_backup_upload.vit_auto_backup_upload'].search([]),
#         })

#     @http.route('/vit_auto_backup_upload/vit_auto_backup_upload/objects/<model("vit_auto_backup_upload.vit_auto_backup_upload"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_auto_backup_upload.object', {
#             'object': obj
#         })