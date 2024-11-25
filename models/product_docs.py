from odoo import models, fields, api

class ProductDocs(models.Model):
    _inherit = "product.document"

    visible_all_variant = fields.Boolean(help="If True Visible in All Variant, Vice Versa in False", string="Visible: in all Variant")
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
