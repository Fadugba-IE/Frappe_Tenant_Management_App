// Copyright (c) 2021, Iyanu Fadugba and contributors
// For license information, please see license.txt

frappe.ui.form.on('Owner', {
    refresh: function(frm) {
        frm.add_custom_button('Create Tenancy Agreement', () => {
            frappe.new_doc('Tenancy Agreement', {
                owner: frm.doc.name
            })
        })
      
    }
});
