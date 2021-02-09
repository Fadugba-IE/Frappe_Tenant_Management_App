# -*- coding: utf-8 -*-
# Copyright (c) 2021, Iyanu Fadugba and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class TenancyAgreement(Document):
	def before_submit(self):
		exists = frappe.db.exists(
			"Tenancy Agreement",
			{
				"Tenant": self.Tenant,
				"docstatus": 1,
				"to_date": (">", self.from_date),
			},
		)
		if exists:
			frappe.throw("There is an Tenacy Agreement for this member")
