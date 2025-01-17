"""honeybee-vtk post-process command."""

import sys
import traceback
import click
from honeybee_vtk.image_processing import write_gif, write_transparent_images


@click.group()
def post_process():
    """Command to post-process media generated by honeybee-vtk."""
    pass


@post_process.command('gif')
@click.argument('images-folder')
@click.option(
    '--folder', '-f', type=click.Path(exists=False, file_okay=False, resolve_path=True,
                                      dir_okay=True),
    default='.', show_default=True, help='Path to target folder.',
)
@click.option(
    '--gradient-transparency/--no-gradient-transparency', default=False,
    show_default=True,
    help='Whether to use a gradient transparency. or not. If chosen a gradient of'
    ' transparency will be used. Which will make the image in the back more transparent'
    ' compared to the image in the front. Defaults to False which will use a flat'
    ' transparency. which means the all images will have same amount of transparency.'
    ' Defaults to using a flat transparency.', is_flag=True
)
@click.option(
    '--duration', '-d', type=int, default=1000, show_default=True,
    help='Duration of each frame in milliseconds. Default is 1000.'
)
@click.option(
    '--loop-count', '-lc', type=int, default=0, show_default=True,
    help='Number of times to loop the gif. Default is 0 which means loop forever.'
)
@click.option(
    '--linger-last-frame', '-llf', type=int, default=3, show_default=True,
    help='An integer that will make the last frame linger for longer than the'
    ' duration. If set to 0, the last frame will not linger. Setting it to 3 will make'
    ' the last frame linger for 3 times the duration. Defaults to 3.'
)
def export_gif(images_folder, folder, gradient_transparency, duration,
               loop_count, linger_last_frame):
    """Write a gif from a set of images.

    \b
    Args:
        images_folder: Path to the folder containing images to create GIF from.
        folder: Path to target folder where the GIF will be written.
        gradient_transparency: Whether to use a gradient transparency. or not. If
            chosen a gradient of transparency will be used. Which will make the image 
            in the back more transparent compared to the image in the front. Defaults
            to False which will use a flat transparency. which means the all images 
            will have same amount of transparency. Defaults to using a flat transparency.
        duration: Duration of each frame in milliseconds. Default is 1000.
        loop_count: Number of times to loop the gif. Default is 0 which means loop
            forever.
        linger_last_frame: An integer that will make the last frame linger for
            longer than the duration. If set to 0, the last frame will not linger.
            Setting it to 3 will make the last frame linger for 3 times the duration.
            Defaults to 3.
    """
    try:
        output = write_gif(images_folder, folder, gradient_transparency,
                           duration, loop_count, linger_last_frame)
    except Exception:
        traceback.print_exc()
        sys.exit(1)
    else:
        print(f'Success: {output}', file=sys.stderr)
        return sys.exit(0)


@post_process.command('transparent-images')
@click.argument('images-folder')
@click.option(
    '--folder', '-f', type=click.Path(exists=False, file_okay=False, resolve_path=True,
                                      dir_okay=True),
    default='.', show_default=True, help='Path to target folder.',
)
@click.option(
    '--transparency', '-t', type=float, default=0.5, show_default=True,
    help='The transparency value to use. Acceptable values are decimal point numbers'
    ' between 0 and 1 inclusive. 0 is completely transparent and 1 is completely opaque.'
    ' Defaults to 0.5.'
)
def export_transparent_images(images_folder, folder, transparency):
    """Write an overlappable transparent image for each images in the images folder.

    \b
    Args:
        images_folder: Path to the folder containing images to transform.
        folder: Path to target folder where the transparent images will be written.
        transparency: The transparency value to use. Acceptable values are decimal point
            numbers between 0 and 1 inclusive. 0 is completely transparent and 1 is
            completely opaque. Defaults to 0.5.
    """
    try:
        output = write_transparent_images(images_folder, folder, transparency)
    except Exception:
        traceback.print_exc()
        sys.exit(1)
    else:
        print(f'Success: {output}', file=sys.stderr)
        return sys.exit(0)
