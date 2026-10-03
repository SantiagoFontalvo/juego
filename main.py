scene.set_background_color(8)
Jugador = sprites.create(assets.image("""
    Jugador
    """), SpriteKind.player)
controller.move_sprite(Jugador, 100, 100)
tiles.set_current_tilemap(tilemap("""
    level1
    """))