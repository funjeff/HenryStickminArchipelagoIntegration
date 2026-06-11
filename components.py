from worlds.LauncherComponents import Component, Type, components, launch as launch_component


def run_client(*args: str) -> None:
    from .client import launch
    launch_component(launch, name="Henry Client", args=args)


components.append(
    Component(
        "Henry Client",
        func=run_client,
        game_name="The Henry Stickmin Collection",
        component_type=Type.CLIENT
    )
)
