/** @odoo-module */

import publicWidget from '@web/legacy/js/public/public_widget';
import { VariantMixin } from '@website_sale/variant_mixin';
import { _t } from "@web/core/l10n/translation";
import { patch } from '@web/core/utils/patch';
import { rpc } from "@web/core/network/rpc";


publicWidget.registry.InheritedVariantMixin = WebsiteSale.extend(VariantMixin, {
    events: {
        'change .css_attribute_color input': '_onChangeColorAttribute',
        'click .o_variant_pills': '_onChangePillsAttribute',
        'change [data-attribute_exclusions]': 'onChangeVariant'
    },


})

export default publicWidget.registry.InheritedVariantMixin;


_getCombinationInfo: function (ev) {
    if ($(ev.target).hasClass('variant_custom_value')) {
        return Promise.resolve();
    }

    const $parent = $(ev.target).closest('.js_product');
    if(!$parent.length){
        return Promise.resolve();
    }
    const combination = this.getSelectedVariantValues($parent);

    return rpc('/website_sale/get_combination_info', {
        'product_template_id': parseInt($parent.find('.product_template_id').val()),
        'product_id': this._getProductId($parent),
        'combination': combination,
        'add_qty': parseInt($parent.find('input[name="add_qty"]').val()),
        'parent_combination': [],
        'context': this.context,
        ...this._getOptionalCombinationInfoParam($parent),
    }).then((combinationData) => {
        if (this._shouldIgnoreRpcResult()) {
            return;
        }

        // console.log("CombinationData.ProductId>>>>>>>>",combinationData.product_id)
        // console.log("COMBINATIONDATA>>>>>>>>",combinationData)
        
        // const productId = combinationData.product_id;
        // $('#product_variant_id').text(productId);
        // $('#product_variant_id').attr('data-product-id', productId);

        // $('.document-item').each(function () {
        //     const documentVariantId = $(this).data('variant-id');
        //     if (documentVariantId === productId) {
        //         $(this).show();
        //     } else {
        //         $(this).hide();
        //     }
        // });

        this._onChangeCombination(ev, $parent, combinationData);
        this._checkExclusions($parent, combination, combinationData.parent_exclusions);
    });
},
