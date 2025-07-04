success_count = 0
failed_messages = []

for move in records:
    try:
        if move.state in ['posted', 'cancel']:
            # Add business logic checks here if needed
            move.button_draft()
            success_count += 1
    except Exception as e:
        failed_messages.append(f"{move.name}: {str(e)}")

# Build notification message
message = f"✅ {success_count} entries reset to draft"
if failed_messages:
    message += f"\n❌ Failed: {', '.join(failed_messages[:3])}"
    if len(failed_messages) > 3:
        message += f" (+{len(failed_messages)-3} more)"

# Assign to 'action' not 'return'
action = {
    'type': 'ir.actions.client',
    'tag': 'display_notification',
    'params': {
        'title': 'Reset Results',
        'message': message,
        'type': 'success' if not failed_messages else 'warning',
        'sticky': bool(failed_messages)  # Keep open if errors
    }
}
## Powered By HSx Tech
## Ali 