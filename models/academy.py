from odoo import models, fields, api
import re
from odoo.exceptions import  ValidationError

class Teacher(models.Model):
    _name = 'teacher.school'
    _description = 'This class is for the teacher profile'
    _rec_name = 'teacher_name'

    teacher_name    = fields.Char(string = "Teacher Name: ")
    teacher_mobile  = fields.Char(string = "Teacher Mobile: ")
    teacher_address = fields.Char(string = "Teacher Address: ")
    teacher_gender  = fields.Selection([('male', 'Male'), ('female', 'Female')], string ='Gender: ')
    teacher_email   = fields.Char(string = "Teacher Email: ")
    teacher_photo   = fields.Image(string='Add Your Photo', max_width=128, max_height=128)
    image_1920      = fields.Image(max_width=128, max_height=128, string='Add Photo')

    @api.constrains('teacher_email')
    def _check_email(self):
        for record in self:
            if record.teacher_email and not re.match(r"[^@]+@[^@]+\.[^@]+", record.teacher_email):
                raise ValidationError('Invalid Email,\nPlease Provide a valid Email ID!!!')

    @api.constrains('teacher_mobile')
    def _check_mobile_number(self):
        for record in self:
            if record.teacher_mobile and not re.match('\\+{0,1}[0-9]{10,12}', record.teacher_mobile):
                raise ValidationError('Invalid Phone Number,\nPlease Provide a valid phone number!!!')
