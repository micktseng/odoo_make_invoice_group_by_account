from odoo import fields, models, api, _

from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT
from odoo.exceptions import UserError

class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'

    advance_payment_method = fields.Selection(selection_add=[('group_by_account', 'Group By Account')],
                                              default='group_by_account')

    @api.multi
    def create_invoices(self):
        if self.advance_payment_method == 'group_by_account':
            sale_orders = self.env['sale.order'].browse(self._context.get('active_ids', []))
            sale_orders.action_invoice_create_group_by_account(final=True)

            if self._context.get('open_invoices', False):
                return sale_orders.action_view_invoice()
            return {'type': 'ir.actions.act_window_close'}
        else:
            return super(SaleAdvancePaymentInv, self).create_invoices()

