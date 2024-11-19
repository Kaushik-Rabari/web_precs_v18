import json
from odoo import http
from odoo.http import request, route, Controller
from odoo.addons.website_sale.controllers.variant import WebsiteSaleVariantController


class WebsiteSaleVariantController(WebsiteSaleVariantController):
    @http.route()
    def get_combination_info_website(self, product_template_id, product_id, combination, add_qty, **kwargs):
        combination_info = super(WebsiteSaleVariantController, self).get_combination_info_website(
            product_template_id, product_id, combination, add_qty, **kwargs
        )

        product = request.env['product.product'].browse(product_id)
        print("\n\nproduct>>>>>>>>>>",product)
        documents = request.env['product.document'].search([('product_document_id', '=', product.id)])
        print("\ndocuments>>>>>>>>>>",documents)

        # combination_info = product._get_combination_info(
        #     combination=request.env['product.template.attribute.value'].browse(combination),
        #     product_id=product_id and int(product_id),
        #     add_qty=add_qty and float(add_qty) or 1.0,
        # )


        document_data = []
        for doc in documents:
            document_data.append({
                'name': doc.name,
                'url': f"/web/content/{doc.id}",
            })
        print("\ndocument_data>>>>>>>>>>",document_data)
        combination_info['product_documents'] = document_data
        print("\ncombination_info>>>>>>>>>>",combination_info,"\n\n")

        return combination_info




        # result = super(WebsiteSaleVariantController, self).get_combination_info_website(**kwargs)        
        # doc_rec = request.env['product.document'].sudo().search([])
        # res=request.env['product.document'].sudo().browse(doc_rec)
        # print("\nRESULT>>>>>>>>>",res," \n")
        # product_docs = request.env['product.document'].sudo().browse()
        # combination_info = product_docs._get_combination_info(
        #     product_docs=product_docs.id,
        # )
        # return result
    

# class WebsiteSaleVariantController(WebsiteSaleVariantController):
#     @route('/website_sale/get_combination_info', type='json', auth='public', methods=['POST'], website=True)
#     def get_combination_info_website(self, product_doc_id, product_template_id, product_id, combination, add_qty, parent_combination=None, **kwargs):

#         product_doc_id = request.env['product.document'].browse('product_document_id')
#         product_documents = request.env['product.document'].search([('product_document_id', '=', product_doc_id.id)])
        
#         result = super(WebsiteSaleVariantController, self).get_combination_info_website(
#             product_doc_id, product_template_id, product_id, combination, add_qty, parent_combination=parent_combination, **kwargs
#         )

#         if product_documents:
#             combination_info = product_doc_id._get_combination_info(
#                 combination=request.env['product.template.attribute.value'].browse(combination),
#                 product_id=product_id and int(product_id),
#                 add_qty=add_qty and float(add_qty) or 1.0,
#                 product_docs=product_documents.id,
#             )

#         return result


# class CustomWebsiteSale(WebsiteSale):

#     @http.route(['/shop/cart/update'], type='json', auth="public", website=True)
#     def cart_update(self, product_id, add_qty=1, **kwargs):
#         # Get product and related documents
#         product = request.env['product.template'].browse(product_id)
#         product_documents = request.env['product.document'].search([('product_id', '=', product.id)])
        
#         # Modify the cart_update method to include your documents
#         response = super(CustomWebsiteSale, self).cart_update(product_id, add_qty, **kwargs)
        
#         # Pass additional data to the response if needed
#         response.update({
#             'product_documents': product_documents
#         })
#         return response


# class WebsiteSaleVariantController(WebsiteSaleVariantController):
#     @http.route()
#     def get_combination_info_website(self, product_document_id, product_template_id, product_id, combination, add_qty, parent_combination=None, **kwargs):

#         product_docs = request.env['product.document'].sudo().browse('product_document_id')
        
#         result = super(WebsiteSaleVariantController, self).get_combination_info_website(
#             product_document_id=product_docs,
#             product_template_id=product_template_id,
#             product_id=product_id,
#             combination=combination,
#             add_qty=add_qty,
#             parent_combination=parent_combination,
#             **kwargs
#         )
        
#         if product_docs:
#             combination_info = product_docs._get_combination_info(
#                 combination=request.env['product.template.attribute.value'].browse(combination),
#                 product_id=product_id and int(product_id),
#                 add_qty=add_qty and float(add_qty) or 1.0,
#                 product_docs=product_docs.id,
#             )

#             result.update({'combination_info': combination_info})
#         return result




# import json
# from odoo import http
# from odoo.http import request, route, Controller
# from odoo.addons.website_sale.controllers.variant import WebsiteSaleVariantController


# class WebsiteSaleVariantController(WebsiteSaleVariantController):
#     @http.route()
#     def get_combination_info_website(self, product_docs, product_template_id, product_id, combination, add_qty,parent_combination=None,**kwargs):
        
#         result = super(WebsiteSaleVariantController, self).get_combination_info_website(self, product_docs, product_template_id, product_id, combination, add_qty,parent_combination=None,**kwargs)
        
#         product_docs = request.env['product.document'].browse(product_document_id)

#         combination_info = product_docs._get_combination_info(
#             combination=request.env['product.template.attribute.value'].browse(combination),
#             product_id=product_id and int(product_id),
#             add_qty=add_qty and float(add_qty) or 1.0,
#             product_docs=product_docs.id,
#         )

#         return result
    
