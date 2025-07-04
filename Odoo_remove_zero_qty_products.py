boms = env['mrp.bom'].browse(env.context.get('active_ids', []))
removed_count = 0

for bom in boms:
    zero_qty_lines = env['mrp.bom.line'].search([
        ('bom_id', '=', bom.id),
        ('product_qty', '=', 0)
    ])
    removed_count += len(zero_qty_lines)
    zero_qty_lines.unlink()

action = {
    'type': 'ir.actions.client',
    'tag': 'display_notification',
    'params': {
        'title': 'Zero Quantity Lines Removed',
        'message': f'Removed {removed_count} zero-quantity line(s) from {len(boms)} BOM(s)',
        'type': 'success',
        'sticky': False,
    }
}
