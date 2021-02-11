# -*- coding: utf-8 -*-
# Copyright (c) 2021, Iyanu Fadugba and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class TenancyAgreement(Document):
	def before_submit(self):
		exists = frappe.db.exists(
			"Tenancy Agreement",
			{
				"tenant": self.tenant,
				"docstatus": 1,
				"due_date": (">", self.start_date),
			},
		)
		if exists:
			frappe.throw("There is a Running Tenacy Agreement for this Tenant, Kindly check the system for more information")
