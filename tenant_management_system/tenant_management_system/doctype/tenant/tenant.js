// Copyright (c) 2021, Iyanu Fadugba and contributors
// For license information, please see license.txt

frappe.ui.form.on('Tenant', {
    refresh: function(frm) {
        frm.add_custom_button('Create Tenancy Agreement', () => {
            frappe.new_doc('Tenancy Agreement', {
                tenant: frm.doc.name
            })
        })
        frm.add_custom_button('Record Rent Payment', () => {
            frappe.new_doc('Payment Transaction', {
                tenant: frm.doc.name
            })
		})
		
    }
});
