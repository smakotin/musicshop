


class ImageUploadHelper:

    FIELD_TO_COMBINE_MAP = {
        'defaults': {
            'upload_postfix': 'uploads'
        },
        'Member': {
            'field': 'slug',
            'upload_postfix': 'members_images'
        },
        'Artist': {
            'field': 'slug',
            'upload_postfix': 'artists_images'
        },
        'Album': {
            'field': 'slug',
            'upload_postfix': 'albums_images'
        },
    }

    def __init__(self, field_name_to_combine, instance, filename, upload_postfix):
        self.field_name_to_combine = field_name_to_combine
        self.instance = instance
        self.extension = filename.split('.')[-1]
        self.upload_postfix = f' {upload_postfix}'

