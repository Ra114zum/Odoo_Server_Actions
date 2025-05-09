# Remove Duplicate Products from BOM Lines
# Part of Odoo BOM Cleanup Tools - Powered by Hsx TECH

def remove_duplicate_products(self):
    """
    Server action to remove duplicate product entries in BOM lines
    Preserves the first occurrence of each product
    """
    boms = self if self else self.env['mrp.bom'].browse(self.env.context.get('active_ids'))
    duplicate_count = 0

    for bom in boms:
        seen = set()
        duplicates = []
        for line in bom.bom_line_ids:
            if line.product_id.id in seen:
                duplicates.append(line.id)
            else:
                seen.add(line.product_id.id)
        
        if duplicates:
            duplicate_count += len(duplicates)
            bom.write({'bom_line_ids': [(3, d) for d in duplicates]})

    return {
        'type': 'ir.actions.client',
        'tag': 'display_notification',
        'params': {
            'title': 'Duplicates Removed',
            'message': f'Removed {duplicate_count} duplicate lines from {len(boms)} BOM(s)',
            'type': 'success',
            'sticky': False,
        }
    }
## Powered By HSx Tech
## Ali 
