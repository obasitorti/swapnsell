from django.core.management.base import BaseCommand
from django.core.files import File
import os
from baseapp.storages_backends import StaticStorage

class Command(BaseCommand):
    help = "Upload all static files under swapandsell/static to S3 via StaticStorage."

    def add_arguments(self, parser):
        parser.add_argument(
            "--base",
            default=os.path.join("swapandsell", "static"),
            help="Base static folder (default: swapandsell/static)"
        )
        parser.add_argument(
            "--prefix",
            default="",
            help="S3 prefix under <bucket>/static/ (e.g. 'swapandsell/')"
        )
        parser.add_argument(
            "--force",
            action="store_true",
            help="Overwrite existing files in S3 (will save anyway)"
        )

    def handle(self, *args, **options):
        base = os.path.abspath(options["base"])
        prefix = options["prefix"].strip("/")
        storage = StaticStorage()

        if not os.path.isdir(base):
            self.stderr.write(self.style.ERROR(f"Base folder not found: {base}"))
            return

        uploaded = 0
        for root, _, files in os.walk(base):
            for fname in files:
                local_path = os.path.join(root, fname)
                rel_path = os.path.relpath(local_path, base).replace(os.sep, "/")
                if prefix:
                    dest = f"{prefix}/{rel_path}"
                else:
                    dest = rel_path
                dest = dest.lstrip("/")
                dest_key = f"static/{dest}"

                with open(local_path, "rb") as f:
                    django_file = File(f)
                    try:
                        storage.save(dest_key, django_file)
                        uploaded += 1
                        self.stdout.write(self.style.SUCCESS(f"Uploaded: {dest_key}"))
                    except Exception as e:
                        self.stderr.write(self.style.ERROR(f"Failed: {dest_key} -> {e}"))

        self.stdout.write(self.style.NOTICE(f"Done. Uploaded {uploaded} files."))
