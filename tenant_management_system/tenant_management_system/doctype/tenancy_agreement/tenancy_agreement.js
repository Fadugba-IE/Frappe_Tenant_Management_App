// Copyright (c) 2021, Iyanu Fadugba and contributors
// For license information, please see license.txt

frappe.ui.form.on('Tenancy Agreement', {
	refresh: function(frm) {
        frm.add_custom_button('Record Payment Transaction', () => {
            frappe.new_doc('Payment Transaction', {
                propert: frm.doc.property
            })
        })  
      
    }
});
