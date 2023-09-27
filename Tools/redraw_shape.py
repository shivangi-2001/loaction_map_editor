import cv2
from Tools.function import  choose_zoneType_color, ros2_to_meters


def redraw_rectangle(map, keepout_map, speed_map, offset_x, offset_y, resolution, tlx, tly, brx, bry, color, call, undo_colored_map, undo_keepout_map, undo_speed_map, steps):
    tlx, tly, brx, bry = float(tlx), float(tly), float(brx), float(bry)
    tx, ty, bx, by = offset_x + float(tlx), offset_y + float(tly), offset_x + float(brx), offset_y + float(bry)
    tx_p, ty_p, bx_p, by_p = int(tx / resolution), int(ty / resolution), int(bx / resolution), int(by / resolution)

    color, keepout_color, speed_color = choose_zoneType_color(call, color)

    if color is not None:
        overlay = map.copy()
        draw_map = cv2.rectangle(overlay, (tx_p, ty_p), (bx_p, by_p), color, -1)
        map = cv2.addWeighted(draw_map, 0.4, map, 1 - 0.4, 0)
    if keepout_color is None:
        pass
    else:
        keepout_map = cv2.rectangle(keepout_map, (tx_p, ty_p), (bx_p, by_p), (keepout_color, keepout_color, keepout_color), -1)
    if speed_color is None:
        pass
    else:
        speed_map = cv2.rectangle(speed_map, (tx_p, ty_p), (bx_p, by_p), (speed_color, speed_color, speed_color), -1)
    undo_colored_map.append(map.copy())
    undo_keepout_map.append(keepout_map.copy())
    undo_speed_map.append(speed_map.copy())
    steps += 1
    return map, keepout_map, speed_map, undo_colored_map, undo_keepout_map, undo_speed_map, steps


def redraw_circle(map, keepout_map, speed_map, x_p, y_p, r, color, call, undo_colored_map, undo_keepout_map, undo_speed_map, steps):
    color, keepout_color, speed_color = choose_zoneType_color(call, color)
    overlay = map.copy()
    draw_map = cv2.circle(overlay, (x_p, y_p), r, color, -1)
    map = cv2.addWeighted(draw_map, 0.4, map, 1 - 0.4, 0)
    if keepout_color is None:
        pass
    else:
        keepout_map = cv2.circle(keepout_map, (int(x_p), int(y_p)), r, (keepout_color, keepout_color, keepout_color), -1)
    if speed_map is None:
        pass
    else:
        speed_map = cv2.circle(speed_map, (int(x_p), int(y_p)), r, (speed_color, speed_color, speed_color), -1)
    undo_colored_map.append(map.copy())
    undo_keepout_map.append(keepout_map.copy())
    undo_speed_map.append(speed_map.copy())
    steps += 1
    return map, keepout_map, speed_map, undo_colored_map, undo_keepout_map, undo_speed_map, steps

def redraw_station(map, height, yaml_data, resolution, ros_x, ros_y, undo_colored_map, undo_keepout_map, undo_speed_map, steps):
    # print(scale_width, scale_height, ros_x, ros_y, "=>", ros_x*scale_width, ros_y*scale_height)
    x_m, y_m = ros2_to_meters(height, yaml_data, ros_x, ros_y)
    x_p, y_p = int(x_m/resolution), int(y_m/resolution)
    map = cv2.circle(map, (x_p, y_p), 15, (255, 0, 0), -1)
    undo_colored_map.append(map.copy())
    undo_keepout_map.append(map.copy())
    undo_speed_map.append(map.copy())
    steps += 1
    return map, undo_colored_map, undo_keepout_map, undo_speed_map, steps

def redraw_docks(map, height, yaml_data, resolution, ros_x, ros_y, undo_colored_map, undo_keepout_map, undo_speed_map, steps):
    x_m, y_m = ros2_to_meters(height, yaml_data, ros_x, ros_y)
    x_p, y_p = int(x_m / resolution), int(y_m / resolution)
    map = cv2.circle(map, (x_p, y_p), 15, (0, 0, 0), -1)
    undo_colored_map.append(map.copy())
    undo_keepout_map.append(map.copy())
    undo_speed_map.append(map.copy())
    steps += 1
    return map, undo_colored_map, undo_keepout_map, undo_speed_map, steps

def redraw_waypoints(map, height, yaml_data, resolution, ros_x, ros_y, undo_colored_map, undo_keepout_map, undo_speed_map, steps):
    x_m, y_m = ros2_to_meters(height, yaml_data, ros_x, ros_y)
    x_p, y_p = int(x_m / resolution), int(y_m / resolution)
    map = cv2.circle(map, (x_p, y_p), 15, (0, 0, 255), -1)
    undo_colored_map.append(map.copy())
    undo_keepout_map.append(map.copy())
    undo_speed_map.append(map.copy())
    steps += 1
    return map, undo_colored_map, undo_keepout_map, undo_speed_map, steps

def redraw_waypoints(map, height, yaml_data, resolution, ros_x, ros_y, undo_colored_map, undo_keepout_map, undo_speed_map, steps):
    x_m, y_m = ros2_to_meters(height, yaml_data, ros_x, ros_y)
    x_p, y_p = int(x_m / resolution), int(y_m / resolution)
    map = cv2.circle(map, (x_p, y_p), 15, (0, 0, 255), -1)
    undo_colored_map.append(map.copy())
    undo_keepout_map.append(map.copy())
    undo_speed_map.append(map.copy())
    steps += 1
    return map, undo_colored_map, undo_keepout_map, undo_speed_map, steps

def redraw_reflector(map, height, yaml_data, resolution, ros_x, ros_y, undo_colored_map, undo_keepout_map, undo_speed_map, steps):
    x_m, y_m = ros2_to_meters(height, yaml_data, ros_x, ros_y)
    x_p, y_p = int(x_m / resolution), int(y_m / resolution)
    start = (x_p - 20, y_p - 25)
    end = (x_p + 20, y_p + 25)
    map = cv2.rectangle(map, start, end, (3, 173, 252), -1)
    undo_colored_map.append(map.copy())
    undo_keepout_map.append(map.copy())
    undo_speed_map.append(map.copy())
    steps += 1
    return map, undo_colored_map, undo_keepout_map, undo_speed_map, steps

def redraw_textnotation(map, text, x_p, y_p, undo_colored_map, undo_keepout_map, undo_speed_map, steps):
    coordinates = (x_p - 15, y_p)
    font = cv2.FONT_HERSHEY_COMPLEX
    fontScale = 1
    color = (255, 0, 255)
    thickness = 2
    map = cv2.putText(map, text, coordinates, font, fontScale, color, thickness, cv2.LINE_AA)
    undo_colored_map.append(map.copy())
    undo_keepout_map.append(map.copy())
    undo_speed_map.append(map.copy())
    steps += 1
    return map, undo_colored_map, undo_keepout_map, undo_speed_map, steps