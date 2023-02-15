cmake_minimum_required(VERSION 2.8.3)
project(serial_test)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  serial
  std_msgs
)


catkin_package(
  CATKIN_DEPENDS 
  	roscpp 
  	serial
  	std_msgs
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(serial_test_node src/serial_test_node.cpp)

target_link_libraries(serial_test_node
	${catkin_LIBRARIES}
)
