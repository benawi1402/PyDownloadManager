from interaction.InteractionManager import InteractionManager
from logger.LogManager import LogManager
import config.ConfigManager

if __name__ == '__main__':
    log = LogManager()

    interaction_manager = InteractionManager()
    parser = interaction_manager.parse_args()





