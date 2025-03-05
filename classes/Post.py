import pygame

from constants import *
from helpers import screen


class Post:
    """
    A class used to represent post on Nitzagram
    """

    def __init__(self, user_name, location="", description=""):
        self.user_name = user_name
        self.location = location
        self.likes_counter = 0
        self.comments = []
        self.description = description

    def add_like(self):
        self.likes_counter += 1

    def add_comment(self, text):
        self.comments.append(Comment(text))

    def display_above(self):
        position_index_user = (USER_NAME_X_POS, USER_NAME_Y_POS)
        position_index_location = (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS)
        position_index_description = (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS)

        font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)

        user_name_to_display = font.render(self.user_name,True, LIGHT_GRAY)
        location_to_display = font.render(self.location, True, LIGHT_GRAY)
        description_to_display = font.render(self.description, True, LIGHT_GRAY)

        screen.blit(user_name_to_display, position_index_user)
        screen.blit(location_to_display, position_index_description)
        screen.blit(description_to_display, position_index_location)

    def display_post(self):
        pass

    def display_under(self):
        position_index_like = (LIKE_BUTTON_X_POS, LIKE_BUTTON_Y_POS)
        position_index_comments = (COMMENT_BUTTON_X_POST, COMMENT_BUTTON_Y_POS)
        position_index_share = (SHARE_BUTTON_X_POST, SHARE_BUTTON_Y_POS)

        font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)

        like_to_display = font.render(self.likes_counter ,True, LIGHT_GRAY)
        comments_to_display = font.render(self.comments, True, LIGHT_GRAY)
        share_to_display = font.render(self.sh)

        screen.blit(like_to_display, position_index_like)
        screen.blit(comments_to_display, position_index_comments)

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break
