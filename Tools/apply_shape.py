import cv2
from sqlite3 import IntegrityError
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Tools.function import choose_zoneType_color


def rectangle(map, keepout_map, speed_map, offset_x, offset_y, TLX, TLY, BRX, BRY, resolution, call, type_zone, undo_colored_map, undo_keepout_map, undo_speed_map, connection, sql, steps):
    if offset_x and offset_y is not None:
        tlx, tly, brx, bry = float(TLX), float(TLY), float(BRX), float(BRY)
        tx, ty, bx, by = offset_x + float(TLX), offset_y + float(TLY), offset_x + float(BRX), offset_y + float(BRY)
        tlx_p, tly_p, brx_p, bry_p = int(tlx / resolution), int(tly / resolution), int(brx / resolution), int(
            bry / resolution)  # convert the coordinates into pixel
        tx_p, ty_p, bx_p, by_p = int(tx / resolution), int(ty / resolution), int(bx / resolution), int(by / resolution)
        color, keepout_color, speed_color = choose_zoneType_color(call, type_zone)
        if color is not None:
            overlay = map.copy()
            draw_map = cv2.rectangle(overlay, (tx_p, ty_p), (bx_p, by_p), color, -1)
            map = cv2.addWeighted(draw_map, 0.3, map, 1 - 0.3, 0)

            if keepout_color is None:
                pass
            else:
                keepout_map = cv2.rectangle(keepout_map, (tx_p, ty_p), (bx_p, by_p),
                                            (keepout_color, keepout_color, keepout_color), -1)
            if speed_color is None:
                pass
            else:
                speed_map = cv2.rectangle(speed_map, (tx_p, ty_p), (bx_p, by_p),
                                          (speed_color, speed_color, speed_color), -1)

            pixmap = QPixmap.fromImage(QImage(map, map.shape[1], map.shape[0], QImage.Format_BGR888))

            undo_colored_map.append(map.copy())
            undo_keepout_map.append(keepout_map.copy())
            undo_speed_map.append(speed_map.copy())

            steps += 1

            connection.execute("""
                INSERT INTO rectangle_shape(zone_type, steps, TL_x, TL_y, BR_x, BR_y, TL_x_meter, TL_y_meter, BR_x_meter, BR_y_meter)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (type_zone, steps, tlx_p, tly_p, brx_p, bry_p, tlx, tly, brx, bry))
            sql.commit()

            return map, keepout_map, speed_map, pixmap, undo_colored_map, undo_keepout_map, undo_speed_map, connection, sql, steps
        return map, keepout_map, speed_map, None, undo_colored_map, undo_keepout_map, undo_speed_map, connection, sql, steps


def circle (map, keepout_map, speed_map, radius_validate, centerX, centerY, radius, resolution, call, type_zone, undo_colored_map, undo_keepout_map, undo_speed_map, steps, shape_zone, connection, sql):
    centerX, centerY = float(centerX), float(centerY)
    center_x_p, center_y_p = int(centerX / resolution), int(centerY / resolution)  # convert the coordinates into pixel
    center = (center_x_p, center_y_p)
    if radius == "":
        radius_validate.setText("Radius is required !")
    else:
        radius_validate.hide()
        radius = float(radius) # given in meter
        radius_p = int(round((radius / resolution)))
        color, keepout_color, speed_color = choose_zoneType_color(call, type_zone)
        if color is not None:
            overlay = map.copy()
            draw_map = cv2.circle(overlay, center, radius_p, color, -1)
            map = cv2.addWeighted(draw_map, 0.4, map, 1 - 0.4, 0)

            if keepout_color is None:
                pass
            else:
                keepout_map = cv2.circle(keepout_map, center, radius_p, (keepout_color, keepout_color, keepout_color), -1)

            if speed_color is None:
                pass
            else:
                speed_map = cv2.circle(speed_map, center, radius_p, (speed_color, speed_color, speed_color),
                                         -1)

            pixmap = QPixmap.fromImage(QImage(map, map.shape[1], map.shape[0], QImage.Format_BGR888))

            undo_colored_map.append(map.copy())
            undo_keepout_map.append(keepout_map.copy())
            undo_speed_map.append(speed_map.copy())

            steps += 1

            connection.execute("""
                    INSERT INTO circle_shape (zone_type, steps, radius, cx, cy, cx_meter, cy_meter, radius_meter) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """, (type_zone, steps, radius_p, center_x_p, center_y_p, centerX, centerY, radius))
            sql.commit()

            return map, keepout_map,speed_map, pixmap, undo_colored_map, undo_keepout_map, undo_speed_map, steps, connection, sql
        return map, keepout_map,speed_map, None, undo_colored_map, undo_keepout_map, undo_speed_map, steps, connection, sql
    return map, keepout_map,speed_map, None, undo_colored_map, undo_keepout_map, undo_speed_map, steps, connection, sql


def station(map, ros_x, ros_y, x_m, y_m, resolution, station_name, level, height, poseZ, poseW, undo_colored_map, undo_keepout_map, undo_speed_map, steps, connection, sql):
    x_p, y_p = int(float(x_m)/resolution), int(float(y_m)/resolution)
    center = (x_p, y_p)
    color = (255,0,0)
    map = cv2.circle(map, center, 15, color, -1)
    undo_colored_map.append(map.copy())
    undo_keepout_map.append(map.copy())
    undo_speed_map.append(map.copy())
    steps += 1
    connection.execute("""
        INSERT INTO station (steps, station_name, x, y, x_meter, y_meter, station_x, station_y, level, height, pose_z, pose_w)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (steps, station_name, x_p, y_p, x_m, y_m, ros_x, ros_y, level, height, float(poseZ), float(poseW)))
    sql.commit()
    return map, undo_colored_map, undo_keepout_map, undo_speed_map, steps, connection, sql

# def add_station(map, x, y, resolution, station_name, add_level, add_height, pose, undo_colored_map, undo_keepout_map, undo_speed_map, steps, connection, station_x, station_y):
#     stationX, stationY = float(x), float(y)
#     stationX_p, stationY_p = int(stationX / resolution), int(stationY / resolution)
#     undo_colored_map.append(map.copy())
#     undo_keepout_map.append(map.copy())
#     undo_speed_map.append(map.copy())
#     connection.executescript("INSERT INTO layout_designer_temp (zone_type, zone_shape) VALUES ('Rack station','station')" )
#     step = connection.execute("SELECT * FROM layout_designer_temp WHERE zone_shape = 'station' ORDER BY steps DESC").fetchone()
#     connection.executescript("""INSERT INTO station_temp (steps, station_name, x, y, level, height, pose, x_meter, y_meter, station_x, station_y) VALUES ('%d','%s','%d','%d','%s','%s','%f','%f','%f','%f','%f')
#                     """ % (step[0], station_name, stationX_p, stationY_p, add_level, add_height, float(pose), stationX, stationY, station_x, station_y))
#     steps += 1
#     print("station:", steps)
#     return map, undo_colored_map, undo_keepout_map, undo_speed_map, steps,connection

def dock(map, ros_x, ros_y, x_m, y_m, dock_name, resolution, station_link, poseZ, poseW, undo_colored_map, undo_keepout_map, undo_speed_map, steps, connection, sql):
    x_p, y_p = int(float(x_m) / resolution), int(float(y_m) / resolution)
    center = (x_p, y_p)
    map = cv2.circle(map, center, 15, (0,0,0), -1)
    undo_colored_map.append(map.copy())
    undo_keepout_map.append(map.copy())
    undo_speed_map.append(map.copy())
    steps += 1
    connection.execute("""
        INSERT INTO docks (steps, dock_name, station_link, dx, dy, dx_meter, dy_meter, dock_x, dock_y, dock_pose_z, dock_pose_w)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (steps, dock_name, station_link, x_p, y_p, x_m, y_m, ros_x, ros_y, float(poseZ), float(poseW)))
    sql.commit()
    return map, undo_colored_map, undo_keepout_map, undo_speed_map, steps, connection, sql

def waypoint(map, ros_x, ros_y, x_m, y_m, waypoint_counter, station1, station2, pose_z, pose_w, call, resolution, undo_colored_map, undo_keepout_map, undo_speed_map, steps, connection, sql):
    x_p, y_p = int(float(x_m)/resolution), int(float(y_m)/resolution)
    if station1 == '' and station2 == '':
        call.ui.way_err.setText("select stations")
        call.ui.way_err.show()
    else:
        map = cv2.circle(map, (x_p, y_p), 15, (0, 0, 255), -1)

        undo_colored_map.append(map.copy())
        undo_keepout_map.append(map.copy())
        undo_speed_map.append(map.copy())

        waypoint_name = "w_" + str(waypoint_counter)
        steps += 1

        connection.execute("""
            INSERT INTO waypoints (name, steps, x_p, y_p, x_m, y_m, ros_x, ros_y, pose_z, pose_w, station_1, station_2)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (waypoint_name, steps, x_p, y_p, x_m, y_m, ros_x, ros_y, pose_z, pose_w, station1, station2))

        sql.commit()

        waypoint_counter += 1
        return map, waypoint_counter, undo_colored_map, undo_keepout_map, undo_speed_map, steps, connection, sql
    return map, waypoint_counter, undo_colored_map, undo_keepout_map, undo_speed_map, steps, connection, sql

def reflector(map, ros_x, ros_y, x_m, y_m, r_name, resolution, undo_colored_map, undo_keepout_map, undo_speed_map, steps, connection, sql):
    rx_p, ry_p = int(float(x_m) / resolution), int(float(y_m) / resolution)
    start = (rx_p - 20, ry_p - 25)
    end = (rx_p + 20, ry_p + 25)
    map = cv2.rectangle(map, start, end, (3, 173, 252), -1)
    undo_colored_map.append(map.copy())
    undo_keepout_map.append(map.copy())
    undo_speed_map.append(map.copy())
    steps += 1
    connection.execute("""
                        INSERT INTO reflector (steps, name, rx_p, ry_p, rx, ry, ros_x, ros_y)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        """, (steps, r_name, rx_p, ry_p, x_m, y_m, ros_x, ros_y))
    sql.commit()
    return map, undo_colored_map, undo_keepout_map, undo_speed_map, steps, connection, sql


def text_notation(map, x_m, y_m, resolution, text, undo_colored_map, undo_keepout_map, undo_speed_map, steps, connection, sql):
    x_p, y_p = int(x_m / resolution), int(y_m / resolution)
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
    connection.execute("""
            INSERT INTO text (steps, name, x_p, y_p) VALUES (?, ?, ?, ?)""", (steps, text, x_p, y_p))
    sql.commit()
    return map, undo_colored_map, undo_keepout_map, undo_speed_map, steps, connection, sql