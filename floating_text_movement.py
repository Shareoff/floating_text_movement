import math
import json
import click


def easeLinear(x):
	return x


def easeInSine(x):
	return 1 - math.cos((x * math.pi) / 2)


def easeOutSine(x):
	return math.sin((x * math.pi) / 2)


def easeInOutSine(x):
	return -(math.cos(math.pi * x) - 1) / 2


def polynomialIn(x, degree):
	return pow(x, degree)


def polynomialOut(x, degree):
	return 1 - pow(1 - x, degree)


def polynomialInOut(x, degree):
	if x < 0.5:
		return pow(2, degree - 1) * polynomialIn(x, degree)
	else:
		return 1 - pow(-2 * x + 2, degree) / 2


QUAD_DEGREE = 2
def easeInQuad(x):
	return polynomialIn(x, QUAD_DEGREE)


def easeOutQuad(x):
	return polynomialOut(x, QUAD_DEGREE)


def easeInOutQuad(x):
	return polynomialInOut(x, QUAD_DEGREE)


CUBIC_DEGREE = 3
def easeInCubic(x):
	return polynomialIn(x, CUBIC_DEGREE)


def easeOutCubic(x):
	return polynomialOut(x, CUBIC_DEGREE)


def easeInOutCubic(x):
	return polynomialInOut(x, CUBIC_DEGREE)


QUART_DEGREE = 4
def easeInQuart(x):
	return polynomialIn(x, QUART_DEGREE)


def easeOutQuart(x):
	return polynomialOut(x, QUART_DEGREE)


def easeInOutQuart(x):
	return polynomialInOut(x, QUART_DEGREE)


QUINT_DEGREE = 5
def easeInQuint(x):
	return polynomialIn(x, QUINT_DEGREE)


def easeOutQuint(x):
	return polynomialOut(x, QUINT_DEGREE)


def easeInOutQuint(x):
	return polynomialInOut(x, QUINT_DEGREE)


def easeInExpo(x):
	return 0 if round(x, 3) == 0 else pow(2, 10 * x - 10)


def easeOutExpo(x):
	return 1 if x == 1 else 1 - pow(2, -10 * x)


def easeInOutExpo(x):
	if x == 0:
		return 0
	if x == 1:
		return 1
	if x < 0.5:
		return pow(2, 20 * x - 10) / 2
	return (2 - pow(2, -20 * x + 10)) / 2


def easeInCirc(x):
	return 1 - math.sqrt(1 - pow(x, 2))


def easeOutCirc(x):
	return math.sqrt(1 - pow(x - 1, 2))


def easeInOutCirc(x):
	if x < 0.5:
		return (1 - math.sqrt(1 - pow(2 * x, 2))) / 2 
	return (math.sqrt(1 - pow(-2 * x + 2, 2)) + 1) / 2


# consts for funi maths lol
C1 = 1.70158
C2 = C1 * 1.525;
C3 = C1 + 1
def easeInBack(x):
	return C3 * x * x * x - C1 * x * x


def easeOutBack(x):
	return 1 + C3 * pow(x - 1, 3) + C1 * pow(x - 1, 2)


def easeInOutBack(x):
	if x < 0.5:
		return (pow(2 * x, 2) * ((C2 + 1) * 2 * x - C2)) / 2
	return (pow(2 * x - 2, 2) * ((C2 + 1) * (x * 2 - 2) + C2) + 2) / 2


C4 = (2 * math.pi) / 3
C5 = (2 * math.pi) / 4.5
def easeInElastic(x):
	if x == 0:
		return 0
	if x == 1:
		return 1
	return -pow(2, 10 * x - 10) * math.sin((x * 10 - 10.75) * C4)


def easeOutElastic(x):
	if x == 0:
		return 0
	if x == 1:
		return 1
	return pow(2, -10 * x) * math.sin((x * 10 - 0.75) * C4) + 1


def easeInOutElastic(x):
	if x == 0:
		return 0
	if x == 1:
		return 1
	if x < 0.5:
		return -(pow(2, 20 * x - 10) * math.sin((20 * x - 11.125) * C5)) / 2
	return (pow(2, -20 * x + 10) * math.sin((20 * x - 11.125) * C5)) / 2 + 1


def easeOutBounce(x):
	N1 = 7.5625;
	D1 = 2.75;

	if x < 1 / D1:
	    return N1 * x * x;
	if x < 2 / D1:
	    return N1 * (x - 1.5 / D1) * (x - 1.5 / D1) + 0.75;
	if x < 2.5 / D1:
	    return N1 * (x - 2.25 / D1) * (x - 2.25 / D1) + 0.9375;
	return N1 * (x - 2.625 / D1) * (x - 2.625 / D1) + 0.984375;


def easeInBounce(x):
	return 1 - easeOutBounce(1 - x)


def easeInOutBounce(x):
	if x < 0.5:
		return (1 - easeOutBounce(1 - 2 * x)) / 2
	return (1 + easeOutBounce(2 * x - 1)) / 2


def get_curr_from_easing(start, end, progress, easing_func):
	return round(start + (end - start) * easing_func(progress), 2)


def get_color_as_hex_values(color):
	return [int(color[val:val + 2], base=16) for val in range(0, len(color), 2)]


def get_curr_from_easing_hex(start, end, progress, easing_func):
	val = int(round(get_curr_from_easing(start, end, progress, easing_func), 0))
	return 0 if val < 0 else 0xff if val > 0xff else val


def get_color_from_easing(start, end, progress, easing_func):
	start_vals = get_color_as_hex_values(start)
	end_vals = get_color_as_hex_values(end)

	return ''.join([format(get_curr_from_easing_hex(i, j, progress, easing_func), '02x') for i, j in zip(start_vals, end_vals)])


BEATS_IN_BAR = 8

def get_bar(starting_bar, starting_beat, curr_time):
	return int(starting_bar + math.floor((starting_beat + curr_time - 1) / BEATS_IN_BAR))


def get_beat(starting_beat, curr_time):
	beat = starting_beat + curr_time
	while beat > BEATS_IN_BAR:
		beat -= BEATS_IN_BAR
	return round(beat, 3)


easings = {'Linear': easeLinear,
		   'InSine': easeInSine,
		   'OutSine': easeOutSine,
		   'InOutSine': easeInOutSine,
		   'InQuad': easeInQuad,
		   'OutQuad': easeOutQuad,
		   'InOutQuad': easeInOutQuad,
		   'InCubic': easeInCubic,
		   'OutCubic': easeOutCubic,
		   'InOutCubic': easeInOutCubic,
		   'InQuart': easeInQuart,
		   'OutQuart': easeOutQuart,
		   'InOutQuart': easeInOutQuart,
		   'InQuint': easeInQuint,
		   'OutQuint': easeOutQuint,
		   'InOutQuint': easeInOutQuint,
		   'InExpo': easeInExpo,
		   'OutExpo': easeOutExpo,
		   'InOutExpo': easeInOutExpo,
		   'InCirc': easeInCirc,
		   'OutCirc': easeOutCirc,
		   'InOutCirc': easeInOutCirc,
		   'InBack': easeInBack,
		   'OutBack': easeOutBack,
		   'InOutBack': easeInOutBack,
		   'InElastic': easeInElastic,
		   'OutElastic': easeOutElastic,
		   'InOutElastic': easeInOutElastic,
		   'InBounce': easeInBounce,
		   'OutBounce': easeOutBounce,
		   'InOutBounce': easeInOutBounce,
		   }
INTERVAL = 0.01


import itertools
anchors_vertical = ["Upper", "Middle", "Lower"]
anchors_horizontal = ["Left", "Center", "Right"]
anchors = [''.join(anchor) for anchor in itertools.product(anchors_vertical, anchors_horizontal)]


@click.command()
@click.option('-t', '--text', type=str, required=True, prompt="Please enter your text", help="Text to write in floating text")
@click.option('-l', '--anim-length', type=float, required=True, prompt="Please enter the animation length in beats", help="Length of the animation")
@click.option('--x-start', type=float, required=True, prompt="Please enter the starting x value", help="The starting x coordinate")
@click.option('--x-end', type=float, required=True, prompt="Please enter the final x value", help="The end x coordinate")
@click.option('--x-easing', type=click.Choice(easings.keys()), default='Linear', required=True, prompt="Please enter the easing you would like to use for the x values movement", help="The easing of the x values movement")
@click.option('--y-start', type=float, required=True, prompt="Please enter the starting y value", help="The starting y coordinate")
@click.option('--y-end', type=float, required=True, prompt="Please enter the final y value", help="The end y coordinate")
@click.option('--y-easing', type=click.Choice(easings.keys()), default='Linear', required=True, prompt="Please enter the easing you would like to use for the y values movement", help="The easing of the y values movement")
@click.option('--bar', type=int, required=True, prompt="Please enter the bar where the animation should start", help="The bar of the start of the animation")
@click.option('--beat', type=float, required=True, prompt="Please enter the beat where the animation should start", help="The beat of the start of the animation")
@click.option('-i', '--interval', type=float, default=INTERVAL, help="The interval of the animation (how often should floating text events occur")
@click.option('--fade-out', type=float, default=INTERVAL * 10, help="How long should it take each floating text to fade out")
@click.option('--room', default=[0], multiple=True, help="which rooms to display this text in")
@click.option('--color-start', default="ffffff", prompt="Please enter the hex color code at start", help="The color of the text at the start")
@click.option('--color-end', default="ffffff", prompt="Please enter the hex color code at end", help="The color of the text at the end")
@click.option('--color-easing', type=click.Choice(easings.keys()), default='Linear', required=True, prompt="Please enter the easing you would like to use for the color change", help="The easing of the color change")
@click.option('--outline-start', default="000000ff", prompt="Please enter the hex color code of the text outline at the start", help="The color of the outline at the start")
@click.option('--outline-end', default="000000ff", prompt="Please enter the hex color code of the text outline at the end", help="The color of the outline at the end")
@click.option('--outline-easing', type=click.Choice(easings.keys()), default='Linear', required=True, prompt="Please enter the easing you would like to use for the outline color change", help="The easing of the outline color change")
@click.option('--angle-start', default=0, prompt="Please enter the starting angle of the text", help="The starting angle of the text")
@click.option('--angle-end', default=0, prompt="Please enter the final angle of the text", help="The final angle of the text")
@click.option('--angle-easing', type=click.Choice(easings.keys()), default='Linear', required=True, prompt="Please enter the easing you would like to use for the angle movement", help="The easing of the angle movement")
@click.option('--output-file', type=click.File(mode='w'), default="output.txt", prompt="Enter a name for the output file. The generated events will be written into the text file for you to surgery into your level")
@click.option('-s', '--size', type=int, default=8, help="The font size of the text")
@click.option('--starting-id', type=int, default=0, help="The starting id for the text event")
@click.option('--anchor', type=click.Choice(anchors), default="MiddleCenter", help="The anchor of the text")
def floating_text_mov(text, anim_length, x_start, x_end, x_easing, y_start, y_end, y_easing,\
	                  bar, beat, interval, fade_out, room, color_start, color_end, color_easing,\
	                  outline_start, outline_end, outline_easing, angle_start, angle_end, angle_easing,\
	                  output_file, size, starting_id, anchor):
	curr_time = 0
	event_id = starting_id
	while round(curr_time, 3) < round(anim_length, 3):
		progress = curr_time / anim_length
		x_pos = get_curr_from_easing(x_start, x_end, progress, easings[x_easing])
		y_pos = get_curr_from_easing(y_start, y_end, progress, easings[y_easing])
		angle = get_curr_from_easing(angle_start, angle_end, progress, easings[angle_easing])
		color = get_color_from_easing(color_start, color_end, progress, easings[color_easing])
		outline = get_color_from_easing(outline_start, outline_end, progress, easings[outline_easing])
		text_for_adv = text + "\n"
		event = {"bar" : get_bar(bar, beat, curr_time),
				 "beat" : get_beat(beat, curr_time),
				 "y": 1,
				 "type": "FloatingText",
				 "rooms": room,
				 "id": event_id,
				 "text": text_for_adv,
				 "times": "",
				 "textPosition": [x_pos, y_pos],
				 "size": size,
				 "angle": angle,
				 "mode": "HideAbruptly",
				 "showChildren": True,
				 "color": color,
				 "outlineColor": outline,
				 "anchor": anchor,
				 "fadeOutRate": fade_out,
				 }
		output_file.write(json.dumps(event) + ",\n")
		event = {"bar" : get_bar(bar, beat, curr_time + interval),
				 "beat" : get_beat(beat, curr_time + interval),
				 "y": 1,
				 "type": "AdvanceText",
				 "id": event_id,
				 }
		output_file.write(json.dumps(event) + ",\n")
		curr_time += interval
		event_id += 1

	click.echo(f"=======\nAll floating text events have been successfully written to {output_file.name}!\nYou may now copy the contents of that file into your .rdlevel file.")


if __name__ == '__main__':
	floating_text_mov()

	