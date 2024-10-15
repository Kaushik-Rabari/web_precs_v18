from odoo import models, fields


class Teacher(models.Model):
    _name = 'teacher.school'
    _description = 'This class for the teacher profile'
    _rec_name = 'teacher_name'

    teacher_name    = fields.Char(string = "Teacher Name: ")
    teacher_mobile  = fields.Char(string = "Teacher Mobile: ")
    teacher_address = fields.Char(string = "Teacher Address: ")
    teacher_gender  = fields.Selection([('male', 'Male'), ('female', 'Female')], string ='Gender: ')
    teacher_email   = fields.Char(string = "Teacher Email: ")
    teacher_photo   = fields.Image(string='Add Your Photo', max_width=128, max_height=128)
    image_1920      = fields.Image(max_width=128, max_height=128, string='Add Photo')
