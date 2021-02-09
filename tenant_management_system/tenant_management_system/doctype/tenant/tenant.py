# -*- coding: utf-8 -*-
# Copyright (c) 2021, Iyanu Fadugba and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class Tenant(Document):
	pass
def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'