BATCH_SIZE = 500
success_moves = env['account.move'].browse()
failed_messages = []

# Filter only eligible moves
eligible_moves = records.filtered(lambda m: m.state in ('posted', 'cancel'))

# Process in chunks of 500
for i in range(0, len(eligible_moves), BATCH_SIZE):
    batch = eligible_moves[i:i + BATCH_SIZE]
    try:
        batch.button_draft()
        success_moves += batch
    except Exception:
        for move in batch:
            try:
                move.button_draft()
                success_moves += move
            except Exception as e:
                failed_messages.append(f"{move.name}: {str(e)}")

# Build notification message
message = f"✅ {len(success_moves)} entries reset to draft"
if failed_messages:
    message += f"\n❌ Failed: {', '.join(failed_messages[:3])}"
    if len(failed_messages) > 3:
        message += f" (+{len(failed_messages)-3} more)"

action = {
    'type': 'ir.actions.client',
    'tag': 'display_notification',
    'params': {
        'title': 'Reset Results',
        'message': message,
        'type': 'success' if not failed_messages else 'warning',
        'sticky': bool(failed_messages)
    }
}
## Powered By HSx Tech
## Ali Muzafar