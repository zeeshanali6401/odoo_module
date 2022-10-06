from odoo import models, fields

class Course(models, Model):
    _name = 'openacademy.course'
    _description = 'Openacademy'

    name = fields.Char(string = 'Course Name')
    description = fields.text('Description', help='add course Description here')