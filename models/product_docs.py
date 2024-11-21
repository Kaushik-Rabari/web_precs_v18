from odoo import models, fields, api

class ProductDocs(models.Model):
    _inherit = "product.document"

    visible_all_variant = fields.Boolean(default=False)
    product_document_id = fields.Many2one('product.product', string='Product Variant',domain="[('product_tmpl_id', '=', product_template_id)]")
    product_template_id = fields.Many2one('product.template', string='Product Template')

    @api.model
    def default_get(self, fields):
        print("\nfields->>>>>>>>>>>>>>>>>>>>>>>",fields)
        res = super(ProductDocs, self).default_get(fields)
        print("res->>>>>>>>>>>>>>>>>>>>>>>>>>",res)
        active_id = self.env.context.get('active_id')
        print("Active_Id->>>>>>>>>>>>>>>>>>>>",active_id)
        if active_id:
            product_template = self.env['product.template'].browse(active_id)
            print("product_template.Active_Id->>>",product_template.id)
            res['product_template_id'] = product_template
            print("Updated res->>>>>>>>>>>>>>>>>>",res,"\n")
        else:
            print("Product template not found\n")
        return res


    # product_document_id = fields.Many2one('product.product', string='Product Document')
    
    # product_document_id = fields.Many2one('product.product', string='Product Variant', domain=lambda self: [('product_tmpl_id', '=', self.env.context.get('default_product_tmpl_id'))])

    # product_tmpl_id = fields.Many2one('product.template', related='product_document_id.product_tmpl_id', string='Product Template', store=True)


# class ProductTemplate(models.Model):
#     _inherit = "product.template"

#     def action_open_documents(self):
#         self.ensure_one()
#         return {
#             'type': 'ir.actions.act_window',
#             'name': 'Documents',
#             'view_mode': 'form',
#             'res_model': 'product.document',
#             'context': {
#                 'default_product_tmpl_id': self.id,
#             },
#             'target': 'current',
#         }

    # @api.model
    # def default_get(self, fields):
    #     res = super(ProductDocs, self).default_get(fields)
    #     active_id = self.env.context.get('active_id')
    #     print("\nActive_ID>>>>>>>>>>>>>>>>",active_id,"\n")
    #     if active_id:
    #         product_template = self.env['product.template'].browse(active_id)
    #         res['product_document_id'] = product_template.product_variant_ids.ids
    #     return res
    

    # @api.onchange('product_document_id')
    # def onchange_product_document_id(self):
    #     active_id = self.env.context.get('active_id')
    #     print("\nActive_ID>>>>>>>>>>>>>>>>",active_id,"\n")
    #     if self.product_document_id:
    #         self.name = self.product_document_id.name


    # @api.model
    # def default_get(self, fields):
    #     res = super(ProductDocs, self).default_get(fields)
    #     active_id = self.env.context.get('active_id')
    #     if active_id:
    #         product_template = self.env['product.template'].browse(active_id)
    #         res['product_document_id'] = product_template.product_variant_ids.ids
    #     return res


    # @api.onchange('product_document_id')
    # def onchange_product_id(self):
    #     if self.name:
    #         return {
    #             'domain': {
    #                 'product_variant_id': [('product_template_id', '=', self.product_id.id)]
    #             }}


    # @api.onchange('product_document_id')
    # def onchange_product_document_id(self):
    #     if self.product_document_id:
    #         self.name = self.product_document_id.name


    # class ProductTemplate(models.Model):
    #     _inherit = 'product.template'

    #     document_ids = fields.One2many('product.document', 'product_document_id', string='Product Documents')
