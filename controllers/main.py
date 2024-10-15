from odoo import http
from odoo.http import request


class Main_Controller(http.Controller):
    @http.route('/custom/url', type='http', auth='user', website=True)
    def show_custom_webpage(self, **kw):
        return http.request.render('website_v18.index', {})
     
    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, **kw):
        return "Hello, world"
    
    # @http.route('/academy/academy1/', type='http', auth='public', website=True)
    # def index2(self, **kw):
    #     teacher_name = http.request.env['teacher.school'].sudo().search([])
    #     print("\n\nteacher_name >>>>>>>>>>>>", teacher_name,"\n\n")    
    #     return http.request.render('website_v18.index2', {
    #         "teacher" : teacher_name    
    #     }) 
    
    @http.route('/teacher/<name>/', auth='public', website=True)
    def teacher(self, name):
        return '<h1>{}</h1>'.format(name)
        # return http.request.render('website_v18.teacher_data', {})
    
    @http.route('/teacher/<int:id>/', auth='public', website=True)
    def teacher_id(self, id):
        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)
        # return http.request.render('website_v18.teacher_data', {})

    # @http.route('/teachers/<model("teacher.school"):teacher_id>/', auth='public', website=True)
    # def teacher(self, teacher):
    #     return http.request.render('webiste_v18.index2', {
    #         'id': teacher
    #     })

    @http.route('/academy/academy1/', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['teacher.school'].sudo().search([])
        print("\n\nTeachers >>>>>>>>>>>>", Teachers,"\n\n")
        return http.request.render('website_v18.teacher_data', {
            'id': Teachers
        })


    @http.route('/myteacher', type='http', auth='public', website=True)
    def teacher_detail_form(self, **kw):
        print("\nEXECUTING.............")
        teacher_rec = request.env['teacher.school'].sudo().search([])
        print("\nTEACHER REC.............",teacher_rec,"\n")
        return http.request.render('website_v18.new_teacher_form_view', {'Teacher_name':teacher_rec})
        
    @http.route('/create/webteacher', type='http', auth='public', website=True)
    def create_teacher(self, **kw):
        print("\nDATA RECEIVED.............", kw, "\n")
        Teacher_vals = {
            'teacher_name' : kw.get('teacher_name') ,
            'teacher_mobile' : kw.get('teacher_mobile') ,
            'teacher_gender' : kw.get('teacher_gender') ,
            'teacher_address' : kw.get('teacher_address') ,
            'teacher_email' : kw.get('teacher_email') ,
            'teacher_photo' : kw.get('teacher_photo') ,
            }

        request.env['teacher.school'].sudo().create(Teacher_vals)
        return http.request.render('website_v18.thankyou_page_template', {})
 