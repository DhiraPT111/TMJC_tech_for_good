"""Library code for the image classifier."""

def ClassifyScreen(screen_image_data: bytes) -> str:
  if screen_image_data:
    return 'Exists'
  else:
    return 'No data'
