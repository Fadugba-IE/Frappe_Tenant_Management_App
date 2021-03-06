# -*- coding: utf-8 -*-
# Copyright (c) 2021, Iyanu Fadugba and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document 

class PaymentTransaction(Document):
	def on_submit(self):
		self.to_balance = self.rent - self.amount_paid
