# Remove Archived Products from BOM Lines
# Part of Odoo BOM Cleanup Tools - Powered by Hsx TECH

def remove_archived_products(self):
    """
    Server action to remove BOM lines containing archived products
    Works on single or multiple BOMs
    """
    boms = self if self else self.env['mrp.bom'].browse(self.env.context.get('active_ids'))
    archived_count = 0

    for bom in boms:
        archived_lines = bom.bom_line_ids.filtered(lambda l: not l.product_id.active)
        if archived_lines:
            archived_count += len(archived_lines)
            bom.write({'bom_line_ids': [(3, l.id) for l in archived_lines]})

    return {
        'type': 'ir.actions.client',
        'tag': 'display_notification',
        'params': {
            'title': 'Archived Products Removed',
            'message': f'Removed {archived_count} archived lines from {len(boms)} BOM(s)',
            'type': 'success',
            'sticky': False,
        }
    }