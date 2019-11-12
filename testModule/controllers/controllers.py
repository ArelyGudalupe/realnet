# -*- coding: utf-8 -*-
from odoo import http

class testModule(http.Controller):
    @http.route('/testModule/testModuleodule/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/testModule/testModule/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('testModule.listing', {
            'root': '/testModule/testModule',
            'objects': http.request.env['testModule.testModule'].search([]),
        })

    @http.route('/testModule/testModule/objects/<model("testModule.testModule"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('testModule.object', {
            'object': obj
        })