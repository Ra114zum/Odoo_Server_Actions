# Combined BOM Cleanup (Archived + Duplicates)
# Part of Odoo BOM Cleanup Tools - Powered by Hsx TECH

def combined_bom_cleanup(self):
    """
    Performs both archived product removal and duplicate cleanup
    """
    boms = self if self else self.env['mrp.bom'].browse(self.env.context.get('active_ids'))
    stats = {'archived': 0, 'duplicates': 0}

    for bom in boms:
        # Remove archived
        archived = bom.bom_line_ids.filtered(lambda l: not l.product_id.active)
        if archived:
            stats['archived'] += len(archived)
            bom.write({'bom_line_ids': [(3, a.id) for a in archived]})
        
        # Remove duplicates
        seen = set()
        duplicates = []
        for line in bom.bom_line_ids:
            if line.product_id.id in seen:
                duplicates.append(line.id)
            else:
                seen.add(line.product_id.id)
        
        if duplicates:
            stats['duplicates'] += len(duplicates)
            bom.write({'bom_line_ids': [(3, d) for d in duplicates]})

    return {
        'type': 'ir.actions.client',
        'tag': 'display_notification',
        'params': {
            'title': 'BOM Cleanup Complete',
            'message': f"""Cleaned {len(boms)} BOM(s):
            - Archived: {stats['archived']} removed
            - Duplicates: {stats['duplicates']} removed""",
            'type': 'success',
            'sticky': True,
        }
    }