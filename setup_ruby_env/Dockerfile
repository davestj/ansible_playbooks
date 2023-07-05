# Base image
FROM fedora:38

# Set environment variables
ENV RUBY_VERSION=3.0.2
ENV RAILS_VERSION=6.1.4

# Install system dependencies
RUN dnf -y update && \
    dnf -y install \
      curl \
      gcc \
      gcc-c++ \
      git \
      gpg \
      make \
      sqlite \
      sqlite-devel \
      zlib \
      zlib-devel \
      nodejs \
      yarn

# Install Ruby using rbenv
RUN curl -fsSL https://github.com/rbenv/rbenv-installer/raw/main/bin/rbenv-installer | bash && \
    echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc && \
    echo 'eval "$(rbenv init -)"' >> ~/.bashrc && \
    source ~/.bashrc && \
    rbenv install $RUBY_VERSION && \
    rbenv global $RUBY_VERSION

# Install Bundler and Rails
RUN gem install bundler && \
    gem install rails --version $RAILS_VERSION

# Create app directory
RUN mkdir -p /app
WORKDIR /app

# Copy Gemfile and Gemfile.lock
COPY Gemfile Gemfile.lock ./

# Install dependencies
RUN bundle install

# Copy the rest of the application code
COPY . .

# Start the Rails server
CMD ["rails", "server", "-b", "0.0.0.0"]
