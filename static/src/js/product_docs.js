/**@odoo-module */

import publicWidget from '@web/legacy/js/public/public_widget';

publicWidget.registry.WebsiteSale.include({
    /**
     * overrided the default _onChangeCombination() to customize as per requirements
     * @override
     */
    _onChangeCombination(ev, $parent, combination) {
        const res = this._super.apply(this, arguments);
        const productId = combination.product_id;
        $('#product_variant_id').text(productId);
        $('#product_variant_id').attr('data-product-id', productId);
        $('.document-item').each(function () {
            const documentVariantId = $(this).data('variant-id');
            if (documentVariantId === productId) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
        return res;
    },
})
