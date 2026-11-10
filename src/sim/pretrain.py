def domain_randomization(cfg, rng):
    mass = rng.uniform(cfg['mass'][0], cfg['mass'][1])
    friction = rng.uniform(cfg['friction'][0], cfg['friction'][1])
    light = rng.uniform(cfg['light'][0], cfg['light'][1])
    return {'mass': mass, 'friction': friction, 'light': light}
