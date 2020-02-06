# -*- coding: utf-8 -*-
from openerp import http
from odoo.http import request
import pdb

class NewPage(http.Controller):

    @http.route('/books',auth='public', website=True)
    def helloworld(self,**kw):
        
        Atentionareas = http.request.env['openacademy.course']
        atentionareas = Atentionareas.search([('name','!=','')])
        
        i = [] 
        for x in atentionareas:
            i.append(x.name) 
 

        return http.request.render('mymodule.checkout', {            
            'names': i,
        })


    @http.route('/signup', auth='public', website=True)
    def reg(self, **kw):

        responseL = http.request.params
        Course = http.request.env['openacademy.course']

        for N,V in responseL.items():
            CourseActivo = Course.search([('name','=',N)]).write({'description': V})
 

        Atentionareas = http.request.env['openacademy.course']
        atentionareas = Atentionareas.search([('name','!=','')])
        
        i = [] 
        for x in atentionareas:
            i.append(x.name) 
 

        return http.request.render('mymodule.checkout', {            
            'names': i,
            'message': 'Gracias por actulizar. Creado por JC',
        })

